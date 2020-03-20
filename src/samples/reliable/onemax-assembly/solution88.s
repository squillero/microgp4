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

    movl	$-20939, %eax
    movl	$-5575, %ebx
    movl	$-31192, %ecx
    movl	$23569, %edx

    shl $195, %ecx
    add %eax, %eax
    shr $146, %ebx
    shr $130, %eax
    sub %ecx, %edx
    cmp %ebx, %eax
    shl $92, %eax
    shr $152, %edx
    shr $163, %ebx
    or %ecx, %ecx
    shl $61, %eax
    shr $122, %ebx
    or %edx, %eax
    jne n18
    shl $237, %edx
n18:
    add %edx, %eax
    or %ebx, %eax
    shl $51, %ebx
    shr $155, %edx
    or %eax, %ebx
    sub %ecx, %ebx
    je n33
    or %edx, %eax
    add %edx, %ecx
    shr $0, %eax
    shl $139, %ecx
    jnc n35
    cmp %ebx, %ecx
    shr $82, %eax
    shl $45, %edx
n33:
    jz n35
    jno n37
n35:
    shl $107, %ecx
    cmp %ecx, %ecx
n37:
    jo n39
    sub %ecx, %ecx
n39:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
