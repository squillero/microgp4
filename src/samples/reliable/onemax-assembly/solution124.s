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

    movl	$-8409, %eax
    movl	$7704, %ebx
    movl	$-5579, %ecx
    movl	$21184, %edx

    sub %edx, %ebx
    sub %ebx, %ebx
    shl $56, %ebx
    ja n14
    je n12
    jnc n19
    jc n14
    xor %ecx, %eax
    ja n17
n12:
    ja n20
    add %ebx, %edx
n14:
    ja n19
    jnc n20
    cmp %ebx, %ebx
n17:
    shr $7, %ecx
    je n19
n19:
    jnc n20
n20:
    add %edx, %edx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
