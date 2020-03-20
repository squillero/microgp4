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

    movl	$3155, %eax
    movl	$-6607, %ebx
    movl	$-15562, %ecx
    movl	$-27193, %edx

    jnc n20
    jnc n9
    sub %edx, %ebx
    or %edx, %ebx
    xor %ebx, %ebx
    jz n17
n9:
    jnc n15
    shr $57, %edx
    shl $187, %ecx
    je n18
    jc n23
    ja n19
n15:
    sub %ecx, %edx
    xor %ebx, %edx
n17:
    shr $119, %ebx
n18:
    shl $79, %eax
n19:
    shr $27, %ebx
n20:
    xor %ebx, %ecx
    add %ecx, %eax
    shl $230, %edx
n23:
    add %ecx, %ebx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
