    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-15754, %eax
    movl	$28414, %ebx
    movl	$4581, %ecx
    movl	$23296, %edx

    shr $140, %ebx
    cmp %eax, %ecx
    shl $1, %edx
    shr $165, %edx
    jnc n16
    jz n30
    jno n24
    or %ecx, %eax
    cmp %ebx, %eax
    and %edx, %edx
    jc n14
n14:
    shl $99, %ecx
    add %eax, %ebx
n16:
    shl $38, %ebx
    je n23
    jc n28
    shr $49, %eax
    or %edx, %eax
    jmp n34
    cmp %ecx, %ecx
n23:
    je n25
n24:
    jo n28
n25:
    jc n26
n26:
    jc n35
    je n29
n28:
    jmp n33
n29:
    jo n30
n30:
    cmp %edx, %eax
    add %eax, %eax
    jnc n34
n33:
    cmp %eax, %ebx
n34:
    ja n35
n35:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
